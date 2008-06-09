%define use_cpu_defs 0
%{!?target_arch: %define target_arch noarch}
%{!?target_vendor: %define target_vendor novendor}
%{!?target_system: %define target_system nosystem}
%{?target_cpu: %define cpu_defs --with-cpu=%{target_cpu} --enable-cxx-flags=-mcpu=%{target_cpu}
               %define use_cpu_defs 1}
%define target_base_arch %(echo "%{target_arch}" | \
  sed -e "s/armeb/arm/g" -e "s/arm64/arm/g" -e "s/s390x/s390/g" -e "s/i[4-6]86/i386/g" -e "s/mipsel/mips/g" -e "s/ppc32/ppc/g" -e "s/powerpc/ppc/g" )
%{!?vendor_name: %define vendor_name %{target_vendor}}
%define target %{target_arch}-%{target_vendor}-%{target_system}
%define glibcversion 2.5.0
%{!?bootstrap: %define bootstrap 0}
%{!?use_softfp: %define use_softfp 0}

%if !%{bootstrap}
Name:           %{target}-gcc
%else
Name:           %{target}-gcc-static
%endif
Version:        4.1.2
Release:        7%{?dist}
Summary:        Cross Compiling GNU GCC targeted at %{target}
Group:          Development/Languages
License:        GPLv2+
URL:            http://gcc.gnu.org/
Source0:        ftp://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-4.1.2-20070626.tar.bz2
Source1:        README-gcc.fedora
Patch0:         arm-linux-soft-float.patch
Patch1:         gcc40-cross-build-fixes.patch
Patch2:         gcc-4.1.2-gcc_eh.patch
Patch3:         gcc-4.1.2-version.patch
Patch4:         gcc-4.1.1-cross_search_paths-1.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
BuildRequires:  %{target}-binutils zlib-devel
Requires:       %{target}-binutils
%if %{bootstrap}
BuildRequires:  %{target}-%{target_system}-kernel-headers
%else
BuildRequires:  %{target}-glibc
Requires:       %{target}-glibc
Obsoletes:      %{target}-gcc-static
%endif

%description
This is a Cross Compiling version of GNU GCC, which can be used to
compile programs for the %{target} platform, instead of for the
native %{_arch} platform.


%if !%{bootstrap}

%package c++
Summary:        Cross Compiling GNU G++ targeted at %{target}
Group:          Development/Languages
Requires:       %{name} = %{version}-%{release}

%description c++
This package contains the Cross Compiling version of g++, which can be used to
compile c++ code for the %{target} platform, instead of for the
native %{_arch} platform.

%endif


%prep
%setup -q -c -a 1
cp -a %{SOURCE1} .
pushd gcc-%{version}*
%if %(test "%{target_base_arch}" = "arm" && echo 1 || echo 0)
#%patch0 -p1
%endif
%patch1 -p1
%if !%{bootstrap}
%patch3 -p1
%patch4 -p1
%else
%patch2 -p1
%endif
sed -i 's/VERSUFFIX ".*"/VERSUFFIX " (%{vendor_name} %{version}-%{release})"/' \
  gcc/version.c
contrib/gcc_update --touch
# Set up the compiler to take the include files from our toolchain
echo "
#undef STARTFILE_PREFIX_SPEC
#define STARTFILE_PREFIX_SPEC \"%{_prefix}/%{target}/lib/\"" >> gcc/config/linux.h
cp gcc/Makefile.in{,.orig}
sed -e "s@\(^CROSS_SYSTEM_HEADER_DIR =\).*@\1 %{_prefix}/%{target}/include@g"     gcc/Makefile.in.orig > gcc/Makefile.in
popd

# Extract %%__os_install_post into os_install_post~
cat << \EOF > os_install_post~
%__os_install_post
EOF

# Generate customized brp-*scripts
cat os_install_post~ | while read a x y; do
case $a in
# Prevent brp-strip* from trying to handle foreign binaries
*/brp-strip*)
  b=$(basename $a)
  sed -e 's,find $RPM_BUILD_ROOT,find $RPM_BUILD_ROOT%_bindir $RPM_BUILD_ROOT%_libexecdir,' $a > $b
  chmod a+x $b
  ;;
esac
done

sed -e 's,^[ ]*/usr/lib/rpm.*/brp-strip,./brp-strip,' \
< os_install_post~ > os_install_post 

%build
%if %{bootstrap}
%define languages 'c'
%else
%define languages 'c,c++'
%endif
mkdir -p build-%{target}-gcc
pushd build-%{target}-gcc
CC="%{__cc} ${RPM_OPT_FLAGS}" \
../gcc-%{version}*/configure --prefix=%{_prefix} \
  --mandir=%{_mandir} --infodir=%{_infodir} \
%if %{bootstrap}
  --with-build-sysroot=%{_builddir}/%{name}-%{version}/sysroot \
  --disable-threads --disable-shared \
%if %{use_softfp}
  --with-float=soft \
%endif
%else
  --enable-long-long --enable-threads=posix \
  --disable-libstdcxx-pch \
  --enable-__cxa_atexit \
  --enable-symvers=gnu \
  --enable-version-specific-runtime-libs \
  --enable-c99 \
  --with-system-zlib \
  --enable-shared \
%endif
  --target=%{target} --enable-languages=%{languages} \
  --disable-libmudflap --disable-libssp --disable-multilib \
%if %{use_cpu_defs}
  %{cpu_defs} \
%endif
  --disable-nls

# In general, building GCC is not smp-safe
%if %{bootstrap}
make all-gcc
%else
make AS_FOR_TARGET="%{target}-as" \
     LD_FOR_TARGET="%{target}-ld"
%endif
popd


%install
rm -rf $RPM_BUILD_ROOT
pushd build-%{target}-gcc
%if %{bootstrap}
make install-gcc DESTDIR=$RPM_BUILD_ROOT
%else
make install DESTDIR=$RPM_BUILD_ROOT
%endif
popd
# we don't want these as we are a cross version
rm -r $RPM_BUILD_ROOT%{_infodir}
rm -r $RPM_BUILD_ROOT%{_mandir}/man7
rm -f  $RPM_BUILD_ROOT%{_libdir}/libiberty.a
# and these aren't usefull for embedded targets
rm -fr $RPM_BUILD_ROOT%{_bindir}/gcc/%{target}/%{version}/install-tools
rm -fr $RPM_BUILD_ROOT%{_libexecdir}/gcc/%{target}/%{version}/install-tools
%if !%{bootstrap}
rm -f $RPM_BUILD_ROOT%{_prefix}/%{target}/lib/libiberty.a
rm -f $RPM_BUILD_ROOT%{_prefix}/%{target}/lib64/libiberty.a
rm -f $RPM_BUILD_ROOT%{_bindir}/gcc/%{target}/%{version}/*.la
%endif

# creating links (<cpu>-<system>) of cross-tools for use with tsrpm
for FILE in $RPM_BUILD_ROOT%{_bindir}/%{target}-*; do
    ln ${FILE} `echo ${FILE} | sed -e "s/\(.*%{version}.*\)%{target}\(.*\)/\1%{target_arch}-%{target_system}\2/g"`
done

%define __os_install_post . ./os_install_post


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc gcc-%{version}*/COPYING gcc-%{version}*/COPYING.LIB
%doc gcc-%{version}*/README README-gcc.fedora
%{_bindir}/%{target}-*
%{_bindir}/%{target_arch}-%{target_system}-*
%{_prefix}/lib*/gcc/%{target}/
%{_libexecdir}/gcc/%{target}/
%{_mandir}/man1/%{target}-*.1.gz

%if !%{bootstrap}

%exclude %{_bindir}/%{target}-?++
%exclude %{_bindir}/%{target_arch}-%{target_system}-?++
%exclude /usr/lib/gcc/%{target}/%{version}/lib*c++.a
%exclude /usr/lib/gcc/%{target}/%{version}/include/c++
%exclude %{_libexecdir}/gcc/%{target}/%{version}/cc1plus
%exclude %{_includedir}/omp.h
%exclude %{_mandir}/man1/%{target}-g++.1.gz


%files c++
%defattr(-,root,root,-)
%{_bindir}/%{target}-?++
%{_bindir}/%{target_arch}-%{target_system}-?++
/usr/lib/gcc/%{target}/%{version}/lib*c++.a
/usr/lib/gcc/%{target}/%{version}/include/c++
%{_libexecdir}/gcc/%{target}/%{version}/cc1plus
%{_mandir}/man1/%{target}-g++.1.gz

%endif


%changelog
* Tue Mar 25 2008 Brian Schueler <brian.schueler@gmx.de> 4.1.2-7
- switched from Linux threads to POSIX threads

* Fri Aug 3 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-6
- Disable bootstrap
- Add "GP2X" to VERSUFFIX
- Link C++ against -lgcc_eh to fix undefined references
- Specify GPL version in License tag

* Thu May 31 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 4.1.2-5
- Merge in avr-gcc cross compile changes

* Thu May 31 2007 Koos Termeulen koostermeulen@gmail.com 4.1.2-4
- Moved kernel-headers to separate package
- Added bootstrap option to define whether we want a bootstrapped gcc or not

* Thu May 10 2007 Koos Termeulen koostermeulen@gmail.com 4.1.2-3
- Added "linux-2.6.21-headers" and "glibc-2.3.5-headers" for bootstrapping gcc
- Glibc-2.3.5 is used because the arm is not supported in version 2.5

* Thu Apr 26 2007 Koos Termeulen koostermeulen@gmail.com 4.1.2-2
- Correction in description
- Changes in ./configure
- Don't remove the devel-files from package
- Removed CFLAGS because it didn't work properly

* Thu Apr 20 2007 Koos Termeulen koostermeulen@gmail.com 4.1.2-1
- Initial release
