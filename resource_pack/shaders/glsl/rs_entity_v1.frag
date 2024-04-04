// __multiversion__
// This signals the loading code to prepend either #version 100 or #version 300
// es as apropriate.

#include "shaders/fragmentVersionCentroidUV.h"
#include "shaders/uniformEntityConstants.h"
#include "shaders/uniformShaderConstants.h"
#include "shaders/util.h"

LAYOUT_BINDING(0) uniform sampler2D TEXTURE_0;
LAYOUT_BINDING(1) uniform sampler2D TEXTURE_1;

#ifdef USE_MULTITEXTURE
LAYOUT_BINDING(2) uniform sampler2D TEXTURE_2;
#endif

varying vec4 light;
varying vec4 fogColor;

#ifdef USE_OVERLAY
// When drawing horses on specific android devices, overlay color ends up being
// garbage data. Changing overlay color to high precision appears to fix the
// issue on devices tested
varying highp vec4 overlayColor;
#endif

vec4 glintBlend(vec4 dest, vec4 source) {
  // glBlendFuncSeparate(GL_SRC_COLOR, GL_ONE, GL_ONE, GL_ZERO)
  return vec4(source.rgb * source.rgb, source.a) + vec4(dest.rgb, 0.0);
}

uniform float TIME;
#define TIMING TIME

void main() {
  vec4 color = vec4(1.0);

#ifndef NO_TEXTURE
#  if !defined(TEXEL_AA) || !defined(TEXEL_AA_FEATURE)
  color = texture2D(TEXTURE_0, uv);
#  else
  color = texture2D_AA(TEXTURE_0, uv);
#  endif // !defined(TEXEL_AA) || !defined(TEXEL_AA_FEATURE)
#endif // NO_TEXTURE

#ifdef USE_OVERLAY
  // use either the diffuse or the OVERLAY_COLOR
  color.rgb = mix(color, overlayColor, overlayColor.a).rgb;
#endif

#ifdef USE_EMISSIVE
  // make glowy stuff
  color *= mix(vec4(1.0), light, color.a);
#else
  color *= light;
#endif

  color.rgb = mix(color.rgb, fogColor.rgb, fogColor.a);

  vec4 center_color = texture2D(TEXTURE_0, uv);
  if (center_color.a == 0.0)
    discard;

#ifdef RS_GLINT
  if (center_color.a >= 0.5 || center_color.a == 0.0) {
    gl_FragColor = vec4(center_color.r, center_color.g, center_color.b,
                        (center_color.a - 0.5) * 2.0);

  } else if (center_color.a >= 0.25) {
    if (center_color.a > 0.375) {
      //(0.375,0.5) 五彩灯效
      gl_FragColor = vec4(sin(TIMING * 3.0) * 0.3 + center_color.r,
                          sin(TIMING * 5.0) * 0.3 + center_color.g,
                          sin(TIMING * 7.0) * 0.3 + center_color.b, 1.0);
    } else {
      //[0.25,0.375] 呼吸灯，alpha越大闪越快
      float seed = sin(TIMING * (2.0 + center_color.a)) * 0.3;
      gl_FragColor = vec4(seed + center_color.r, seed + center_color.g,
                          seed + center_color.b, 1.0);
    }

  } else {
    if (center_color.a > 0.125) {
      //(0.125,0.25) 呼吸灯,较快
      float seed = sin(TIMING * 10.0) * 0.5;
      gl_FragColor = vec4(seed + center_color.r, seed + center_color.g,
                          seed + center_color.b, 1.0);
    } else {
      //(0,0.125] 发光效果
      gl_FragColor = glintBlend(
          center_color, vec4(center_color.rgb, (0.125 - center_color.a) * 8.0));
    }
  }
#endif
}
