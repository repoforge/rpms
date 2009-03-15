# $Id$
# Authority: dag
# Upstream: 

### Prevent the plugins from being stripped and disabled
%define __spec_install_post /usr/lib/rpm/brp-compress || :

Summary: C++ High Performance Arbitrary Precision Arithmetic Package
Name: aptest
Version: 0.0.1
Release: 3
License: Redistributable, non-commercial use only
Group: Applications/Engineering
URL: http://www.apfloat.org/apfloat/

Source0: http://www.apfloat.org/apfloat/aptestlm.zip
Source1: http://www.apfloat.org/apfloat/aptestll.zip
Source2: http://www.apfloat.org/apfloat/aptestlx.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
ExclusiveArch: %{ix86} x86_64

%description
Apfloat is a C++ arbitrary precision arithmetic package. Multiplications are
done using Fast Fourier Transforms for O(n log n) complexity. The transforms
are done as Number Theoretic Transforms to avoid round-off problems. Three
different moduli are used for optimal memory usage. The final result is
achieved using the Chinese Remainder Theorem. The algorithms are optimized
for very high precision (more than 100 000 digits). The package is written to
be easily portable, but also includes assembler optimization in critical parts
for various processors for maximum performance. The software is released as
freeware and is free for non-commercial use.

%prep
%setup -c -T

unzip -u %{SOURCE0}
%{__mv} -vf aptestm aptestm-fast
%{__mv} -vf config config-fast
%{__mv} -vf readme.txt readme-fast.txt

unzip -u %{SOURCE1}
%{__mv} -vf aptestm aptestm-slow
%{__mv} -vf config config-slow
%{__mv} -vf readme.txt readme-slow.txt

%ifarch x86_64
unzip -u %{SOURCE2}
%{__mv} -vf aptest aptest64
%{__mv} -vf config config64.txt
%{__mv} -vf readme.txt readme64.txt
%endif

%build

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 aptestm-fast %{buildroot}%{_bindir}/aptestm-fast
%{__install} -Dp -m0755 aptestm-slow %{buildroot}%{_bindir}/aptestm-slow

%ifarch x86_64
%{__install} -Dp -m0755 aptest64 %{buildroot}%{_bindir}/aptest64
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc config* readme*.txt
%{_bindir}/aptestm-fast
%{_bindir}/aptestm-slow

%ifarch x86_64
%{_bindir}/aptest64
%endif

%changelog
* Mon Feb 23 2009 Dag Wieers <dag@wieers.com> - 0.0.1-3
- Also added config and readme from all versions.

* Mon Feb 23 2009 Dag Wieers <dag@wieers.com> - 0.0.1-2
- Merge multithread x86 version in x86_64 package.

* Fri Feb 20 2009 Dag Wieers <dag@wieers.com> - 0.0.1-1
- Initial package. (using DAR)
