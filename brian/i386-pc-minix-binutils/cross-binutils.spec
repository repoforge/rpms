%{!?target_arch: %define target_arch noarch}
%{!?target_vendor: %define target_vendor novendor}
%{!?target_system: %define target_system nosystem}
%define target %{target_arch}-%{target_vendor}-%{target_system}

Name:           %{target}-binutils
Version:        2.16.1
Release:        1%{?dist}
Summary:        Cross Compiling GNU binutils targeted at %{target}
Group:          Development/Tools
License:        GPL
URL:            http://www.gnu.org/software/binutils/
Source0:        ftp://ftp.gnu.org/pub/gnu/binutils/binutils-%{version}.tar.bz2
Source1:        README-binutils.fedora
Patch1: binutils-2.16.1-ltconfig-multilib.patch
Patch3: binutils-2.16.1-place-orphan.patch
Patch5: binutils-2.16.1-elfvsb-test.patch
Patch7: binutils-2.16.1-build-fixes.patch
Patch104:       binutils-2.16-posix-1.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
BuildRequires:  texinfo >= 4.0, dejagnu, gettext, flex, bison, gcc

%description
This is a Cross Compiling version of GNU binutils, which can be used to
assemble and link binaries for the %{target} platform, instead of for the
native %{_arch} platform.


%prep
%setup # -q -c
pushd binutils-%{version}
%patch1 -p0 -b .ltconfig-multilib~
%patch3 -p0 -b .place-orphan~
%patch5 -p0 -b .elfvsb-test~
%patch7 -p0 -b .build-fixes~
%patch104 -p1
popd
cp %{SOURCE1} .


%build
mkdir -p build
pushd build
%define host %(echo ${MACHTYPE} | sed "s/$(echo ${MACHTYPE} | cut -d- -f2)/cross/")
../binutils-%{version}/configure --prefix=%{_prefix} --target=%{target} \
  --mandir=%{_mandir} --infodir=%{_infodir} --host=%{host} \
  --with-lib-path=%{_prefix}/%{target}/lib --disable-shared \
  --disable-nls
make configure-host
make 
popd build

%install
rm -rf $RPM_BUILD_ROOT
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
popd build
# these are for win targets only
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/%{target}-{dlltool,nlmconv,windres}.1
# we don't want these as we are a cross version
rm -fr $RPM_BUILD_ROOT%{_infodir}
rm -f   $RPM_BUILD_ROOT%{_libdir}/libiberty.a


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc binutils-%{version}/COPYING binutils-%{version}/COPYING.LIB
%doc binutils-%{version}/README README-binutils.fedora
%{_prefix}/%{target}
%{_bindir}/%{target}-*
%{_mandir}/man1/%{target}-*.1.gz


%changelog
