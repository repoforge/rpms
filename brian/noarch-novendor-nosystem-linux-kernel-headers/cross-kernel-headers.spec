%{!?target_arch: %define target_arch noarch}
%{!?target_vendor: %define target_vendor novendor}
%{!?target_system: %define target_system nosystem}
%define target %{target_arch}-%{target_vendor}-%{target_system}
%define target_base_arch %(echo "%{target_arch}" | \
  sed -e "s/armeb/arm/g" -e "s/arm64/arm/g" -e "s/s390x/s390/g" -e "s/i[4-6]86/i386/g" -e "s/mipsel/mips/g" -e "s/ppc32/ppc/g" -e "s/powerpc/ppc/g" )

Name:           %{target}-linux-kernel-headers
Version:        2.6.18
Release:        1%{?dist}
Summary:        Kernel headers for Cross Compiling to %{target}
Group:          Development/Languages
License:        GPL
URL:            http://ep09.pld-linux.org/~mmazur/linux-libc-headers/
Source0:        http://ep09.pld-linux.org/~mmazur/linux-libc-headers/linux-libc-headers-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
BuildArch:      noarch

%description
Kernel headers for Cross Compiling to %{target}.


%prep
%setup -q -n linux-libc-headers-%{version}


%build
# nothing to build, headers only

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}/%{target}/include
cp -RHp include/asm-%{target_base_arch} $RPM_BUILD_ROOT%{_prefix}/%{target}/include/asm
cp -RHp include/{asm-*,linux}   $RPM_BUILD_ROOT%{_prefix}/%{target}/include/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc doc/*
%{_prefix}/%{target}


%changelog
* Thu Apr 20 2007 Koos Termeulen koostermeulen@gmail.com 2.6.12.0-1
- Initial release
