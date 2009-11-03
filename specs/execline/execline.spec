# $Id$
# Authority: dag

%define _bindir /bin

Summary: Light non-interactive scripting language
Name: execline
Version: 1.06
Release: 1%{?dist}
License: BSD
Group: System Environment/Shells
URL: http://www.skarnet.org/software/execline/

Source: http://www.skarnet.org/software/execline/execline-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: dietlibc-devel >= 0.28
BuildRequires: skalibs-devel >= 0.40

%description
execline is a very light, non-interactive scripting language, which is 
similar to a shell. Simple shell scripts can be easily rewritten in the 
execline language, improving performance and memory usage. execline was 
designed for use in embedded systems, but works on most Unix flavors.

%prep
%setup -n admin/%{name}-%{version}

%build
#COMP="diet gcc"
#COMP="gcc"

#echo "$COMP -O2 -W -Wall -fomit-frame-pointer -pipe" > conf-compile/conf-cc
echo "gcc ${optflags}" >conf-compile/conf-cc
#echo "$COMP -Os -static -s" > conf-compile/conf-ld
echo "linux-:%{_target_cpu}-:" > src/sys/systype
echo "%{_includedir}/skalibs" > conf-compile/import
echo "%{_libdir}/skalibs" >> conf-compile/import
package/compile

%install
%{__rm} -rf %{buildroot}

%{__install} -d -m0755 %{buildroot}%{_bindir}
for cmd in $(cat package/command.exported) ;  do
	%{__install} -Dp -m0755 command/$cmd %{buildroot}%{_bindir}/$cmd
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc package/CHANGES package/README doc/*.html
%{_bindir}/*

%changelog
* Mon Jan 29 2007 Dag Wieers <dag@wieers.com> - 1.06-1
- Initial package. (using DAR)
