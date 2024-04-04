vec2 hash(vec2 x) {
  // standard Perlin noise
  float s = mod(x.x + x.y, 2.) * 2. - 1.; // flow noise checkered rotation direction
                                          // flow noise universal rotation direction
                                          // same rotation speed at all scales
  s *= TIME / _z;                         // rotation speed increase with small scale
  const vec2 k = vec2(.3183099, .3678794);
  x = x * k + k.yx;
  return (-1. + 2. * fract(16. * k * fract(x.x * x.y * (x.x + x.y)))) * mat2(cos(s + vec4(0, 33, 11, 0))); // rotating gradients. rot: https://www.shadertoy.com/view/XlsyWX
}

float noise(vec2 p) {
  vec2 i = floor(p), f = fract(p), u = f * f * (3. - 2. * f);

#define P(x, y) dot(hash(i + vec2(x, y)), f - vec2(x, y))
  return mix(mix(P(0, 0), P(1, 0), u.x), mix(P(0, 1), P(1, 1), u.x), u.y);
}

float perlin(vec2 p) // fractal noise
{
  mat2 m = mat2(2.); // mat2( 1.6,  1.2, -1.2,  1.6 );
  float v = 0., s = 1.;
  for (int i = 0; i < 7; i++, s /= 2.) {
    _z = s; // for flownoise
    v += s * noise(p);
    p *= m;
  }
  return v;
}
