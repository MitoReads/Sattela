#include "core.h"

void preciseSleep(double ms) {
  double frequency = [] {
    LARGE_INTEGER f;
    QueryPerformanceFrequency(&f);
    return static_cast<double>(f.QuadPart) / 1000.0;
  }();

  LARGE_INTEGER start;
  QueryPerformanceCounter(&start);

  while (true) {
    LARGE_INTEGER now;
    QueryPerformanceCounter(&now);
    double elapsed =
        static_cast<double>(now.QuadPart - start.QuadPart) / frequency;
    if (elapsed >= ms) break;
    Sleep(0);  // yield, don't peg the CPU
  }
}