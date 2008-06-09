%{!?target_arch: %define target_arch noarch}
%{!?target_vendor: %define target_vendor novendor}
%{!?target_system: %define target_system nosystem}
%define target %{target_arch}-%{target_vendor}-%{target_system}
%define host %(echo ${MACHTYPE} | sed "s/$(echo ${MACHTYPE} | cut -d- -f2)/cross/")

Name:           %{target}-glibc
Version:        2.5.0
Release:        4%{?dist}
Summary:        Cross Compiled GNU C Library targeted at %{target}
Group:          Development/Languages
License:        LGPLv2+
URL:            http://www.gnu.org/software/libc/
Source0:        ftp://ftp.gnu.org/gnu/glibc/glibc-2.5-20061008T1257.tar.bz2
Source1:        ftp://ftp.gnu.org/gnu/glibc/glibc-ports-2.5.tar.bz2
Source2:        README-glibc.fedora
Patch100:       glibc-2.5-mips_fixes-1.patch
Patch101:       glibc-2.5-libgcc_eh-1.patch
Patch102:       glibc-2.5-localedef_segfault-1.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
BuildRequires:  %{target}-gcc-static %{target}-%{target_system}-kernel-headers
BuildArch:      noarch
Requires:       %{target}-%{target_system}-kernel-headers

%description
This is a Cross Compiled version of the GNU C Library, which can be used to
compile and link binaries for the %{target} platform, instead of for the
native %{_arch} platform.


%prep
%setup -q -c -a 2
pushd glibc-2.5-20061008T1257
tar -xf %{SOURCE1} 
mv glibc-ports-2.5 ports
%patch100 -p1
%patch102 -p1
cp nscd/Makefile{,.orig}
  sed -e "/nscd_stat.o: sysincludes = # nothing/d" nscd/Makefile.orig >     nscd/Makefile
popd
cp -a %{SOURCE2} .


%build
mkdir -p build-%{target}-glibc
pushd build-%{target}-glibc
# CFLAGS not used, maybe we should ?
echo "libc_cv_forced_unwind=yes" > config.cache
echo "libc_cv_c_cleanup=yes" >> config.cache
  BUILD_CC="gcc" CC="%{target}-gcc" \
  AR="%{target}-ar" RANLIB="%{target}-ranlib" \
../glibc-2.5-20061008T1257/configure --prefix=%{_prefix}/%{target} \
  --host=%{target} \
  --build=%{host} --disable-profile --enable-add-ons \
  --with-tls --enable-kernel=2.6.9 --with-__thread \
  --without-fp --without-selinux \
  --with-binutils=%{_prefix}/%{target}/bin \
  --with-headers=%{_prefix}/%{target}/include \
  --cache-file=config.cache
make %{?_smp_mflags}

# generate stubs.h
for i in io math misc posix stdlib streams; do
  make -C ../glibc-2.5-20061008T1257/$i objdir=`pwd` stubs
  cat $i/stubs >> subdir-stubs.h
done

sed '/^@/d' < ../glibc-2.5-20061008T1257/include/stubs-prologue.h > stubs.h
sort subdir-stubs.h >> stubs.h

popd


%install
rm -rf $RPM_BUILD_ROOT
pushd build-%{target}-glibc
make install install_root=$RPM_BUILD_ROOT
#make install-lib-all install_root=$RPM_BUILD_ROOT
#make install-headers install_root=$RPM_BUILD_ROOT
install -m 644 bits/stdio_lim.h $RPM_BUILD_ROOT%{_prefix}/%{target}/include/bits
#install -m 644 stubs.h $RPM_BUILD_ROOT%{_prefix}/%{target}/include/gnu
popd

# despite us being noarch redhat-rpm-config insists on stripping our files
# and on running find-debuginfo.sh on our files
%define __debug_install_post %{nil}
%define __os_install_post /usr/lib/rpm/redhat/brp-compress

# stop rpm from claiming we provide and need native glibc symbols <sigh>
%define _use_internal_dependency_generator 0
%define __find_requires %{nil}
%define __find_provides %{nil}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc glibc-2.5-20061008T1257/BUGS glibc-2.5-20061008T1257/C* glibc-2.5-20061008T1257/FAQ
%doc glibc-2.5-20061008T1257/LICENSES glibc-2.5-20061008T1257/README
%doc glibc-2.5-20061008T1257/README.libm README-glibc.fedora
%doc %{_prefix}/%{target}/info
%{_prefix}/%{target}/include/*
%{_prefix}/%{target}/lib
%{_prefix}/%{target}/bin
%{_prefix}/%{target}/etc
%{_prefix}/%{target}/libexec
%{_prefix}/%{target}/sbin
%{_prefix}/%{target}/share


%changelog
* Sun Aug  5 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3.6-4
- Do NOT provide and require native glibc symbols <sigh>

* Fri Aug  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3.6-3
- Change License tag to: LGPLv2+
- Don't own %%{_prefix}/%%{target} and %%{_prefix}/%%{target}/include dirs, as
  these are already owned by the required arm-gp2x-linux-kernel-headers rpm

* Thu May 31 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.3.6-2
- Merge in latest avr-libc changes (make noarch, don't strip files)

* Thu Apr 25 2007 Koos Termeulen koostermeulen@gmail.com 2.3.6-1
- Initial release
