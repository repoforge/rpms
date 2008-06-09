%{!?target_arch: %define target_arch noarch}
%{!?target_vendor: %define target_vendor novendor}
%{!?target_system: %define target_system nosystem}
%define target %{target_arch}-%{target_vendor}-%{target_system}

Name:           %{target}-binutils
Version:        2.17.50.0.6
Release:        1%{?dist}
Summary:        Cross Compiling GNU binutils targeted at %{target}
Group:          Development/Tools
License:        GPL
URL:            http://www.gnu.org/software/binutils/
Source0:        ftp://ftp.gnu.org/pub/gnu/binutils/binutils-%{version}.tar.bz2
Source1:        README-binutils.fedora
Patch1: binutils-2.17.50.0.6-ltconfig-multilib.patch
Patch2: binutils-2.17.50.0.6-ppc64-pie.patch
Patch3: binutils-2.17.50.0.6-place-orphan.patch
Patch4: binutils-2.17.50.0.6-ia64-lib64.patch
Patch5: binutils-2.17.50.0.6-elfvsb-test.patch
Patch6: binutils-2.17.50.0.6-standards.patch
Patch7: binutils-2.17.50.0.6-build-fixes.patch
Patch8: binutils-2.17.50.0.6-kept-section.patch
Patch9: binutils-2.17.50.0.6-power6-insns.patch
Patch10: binutils-2.17.50.0.6-fixsyms.patch
Patch11: binutils-2.17.50.0.6-gas-debug-ranges-revert.patch
Patch12: binutils-2.17.50.0.6-popcnt.patch
Patch13: binutils-2.17.50.0.6-rh223181.patch
Patch14: binutils-2.17.50.0.6-tekhex.patch
Patch15: binutils-2.17.50.0.6-bz4267.patch
Patch16: binutils-2.17.50.0.6-ppc-relbrlt-test.patch
Patch17: binutils-2.17.50.0.6-rh235221.patch
Patch18: binutils-2.17.50.0.6-sse4.patch
Patch19: binutils-2.17.50.0.6-ppc64-version-script.patch
Patch20: binutils-2.17.50.0.6-rh241252.patch
#Patch100:       http://kegel.com/crosstool/crosstool-0.43/patches/binutils-2.16.1/binutils-2.15-psignal.patch
#Patch101:       http://kegel.com/crosstool/crosstool-0.43/patches/binutils-2.16.1/binutils-skip-comments.patch
#Patch102:       http://kegel.com/crosstool/crosstool-0.43/patches/binutils-2.16.1/cross-gprof.patch
#Patch103:       binutils-2.16.1-fortify-source.patch
Patch104:       binutils-2.17-posix-1.patch
Patch105:       binutils-2.17.50.0.6-target-minix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
BuildRequires:  texinfo >= 4.0, dejagnu, gettext, flex, bison, gcc

%description
This is a Cross Compiling version of GNU binutils, which can be used to
assemble and link binaries for the %{target} platform, instead of for the
native %{_arch} platform.


%prep
%setup -q -c
pushd binutils-%{version}
%patch1 -p0 -b .ltconfig-multilib~
%patch3 -p0 -b .place-orphan~
%patch5 -p0 -b .elfvsb-test~
%patch6 -p0 -b .standards~
%patch7 -p0 -b .build-fixes~
%patch8 -p0 -b .kept-section~
%patch10 -p0 -b .fixsyms~
%patch12 -p0 -b .popcnt~
#%patch13 -p0 -b .rh223181~
#%patch15 -p0 -b .bz4267~
#%patch20 -p0 -b .rh241252~
%patch104 -p1
%patch105 -p1
popd
cp %{SOURCE1} .


%build
mkdir -p build
pushd build
%define host %(echo ${MACHTYPE} | sed "s/$(echo ${MACHTYPE} | cut -d- -f2)/cross/")
../binutils-%{version}/configure --prefix=%{_prefix} --host=%{host} \
  --target=%{target} --mandir=%{_mandir} --infodir=%{_infodir} \
  --with-lib-path=%{_prefix}/%{target}/lib --disable-nls \
  --enable-shared --disable-multilib
make configure-host
make 
popd build


%install
rm -rf $RPM_BUILD_ROOT
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
popd build
# these are for win targets only
rm  $RPM_BUILD_ROOT%{_mandir}/man1/%{target}-{dlltool,nlmconv,windres}.1
# we don't want these as we are a cross version
rm -r $RPM_BUILD_ROOT%{_infodir}
rm    $RPM_BUILD_ROOT%{_libdir}/libiberty.a


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc binutils-%{version}/COPYING binutils-%{version}/COPYING.LIB
%doc binutils-%{version}/README README-binutils.fedora
%{_prefix}/%{target}
%{_bindir}/%{target}-*
/usr/%{host}
%{_mandir}/man1/%{target}-*.1.gz


%changelog
* Mon Jun  4 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.16.1-2
- Add a patch from rtems fixing the issues when building with
  -DFORTIFY_SOURCE=2, thanks Ralf!

* Thu May 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.16.1-1
- Revert to GNU 2.16.1 release as that is what open2x uses and glibc-2.3.6
  doesn't compile with newer binutils
- Merge in all changes from avr-binutils
- Add various patches from the crosstool project (also used by open2x):
  http://open2x.svn.sourceforge.net/viewvc/open2x/trunk/toolchain-new/patches/binutils-2.16.1/

* Sun Apr  1 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.17.50.0.12-1
- Bump to 2.17.50.0.12, to sync with rawhide / Fedora 7
- "Dynamicly Generate" README.fedora so that macros can be used

* Thu Mar 29 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.17.50.0.9-1
- Bump to 2.17.50.0.9
- Use %%configure instead of ./configure
- Various fixups

* Wed Mar 28 2007 Koos Termeulen koostermeulen@gmail.com 2.17-1
- New version and some changes after unofficial review by Hans de Goede

* Wed Mar 21 2007 Koos Termeulen koostermeulen@gmail.com 2.16.1-1
- Initial release
