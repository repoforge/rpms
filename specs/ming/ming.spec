# $Id$
# Authority: dag

%{?rh7:%define _without_python 1}
%{?el2:%define _without_python 1}

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%if %{!?_without_python:1}0
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_includedir %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_inc()')
%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')
%define python_libdir %(%{__python} -c 'import distutils.sysconfig, os.path; print os.path.dirname(distutils.sysconfig.get_python_lib(1))')
%endif

Summary: SWF output library
Name: ming
Version: 0.3.0
Release: 3%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.libming.org/

Source0: http://dl.sf.net/ming/ming-%{version}.tar.gz
Source1: http://dl.sf.net/ming/ming-perl-%{version}.tar.gz
Source2: http://dl.sf.net/ming/ming-py-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, perl, bison, flex, libpng-devel, libungif-devel, perl(ExtUtils::MakeMaker)
%{!?_without_python:BuildRequires: python-devel}

%description
Ming is a c library for generating SWF ("Flash") format movies. This
package only contains the basic c-based library - not yet extensions for
Python, Ruby, etc.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n perl-ming
Summary: Ming perl module
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: perl
Obsoletes: ming-perl

%description -n perl-ming
Ming perl module - perl wrapper for Ming library.

%package -n python-ming
Summary: Ming Python module
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: python = %{python_version}
Obsoletes: ming-python

%description -n python-ming
Ming Python module.

%prep
%setup -b1 -b2

%build
%{__make} %{?_smp_mflags} all static \
	CC="%{__cc}" \
	LIBDIR=%{_libdir} \
	CFLAGS="%{optflags} -fPIC -I. -I.. -I../src"

cd perl_ext
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} OPTIMIZE="%{optflags}"
cd -

%if %{!?_without_python:1}0
%{__make} -C py_ext \
	CC="%{__cc}" \
	CFLAGS="%{optflags}" \
	PYINCDIR="%{python_includedir}"
%endif

%{__make} %{?_smp_mflags} -C util listaction listfdb listjpeg listmp3 listswf makefdb swftophp \
	CC="%{__cc} %{optflags}"

%install
%{__rm} -rf %{buildroot}
%{makeinstall} install-static \
	PREFIX="%{buildroot}%{_prefix}" \
	LIBDIR="%{buildroot}%{_libdir}"

%{__install} -Dp -m0755 util/listaction %{buildroot}%{_bindir}/listaction
%{__install} -Dp -m0755 util/listfdb %{buildroot}%{_bindir}/listfdb
%{__install} -Dp -m0755 util/listjpeg %{buildroot}%{_bindir}/listjpeg
%{__install} -Dp -m0755 util/listmp3 %{buildroot}%{_bindir}/listmp3
%{__install} -Dp -m0755 util/listswf %{buildroot}%{_bindir}/listswf
%{__install} -Dp -m0755 util/makefdb %{buildroot}%{_bindir}/makefdb
%{__install} -Dp -m0755 util/swftophp %{buildroot}%{_bindir}/swftophp

%{__chmod} 0755 %{buildroot}%{_libdir}/libming.so*

%{__make} -C perl_ext install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%if %{!?_without_python:1}0
#%{__install} -d -m0755 %{buildroot}%{python_libdir}
%{__make} -C py_ext install PREFIX="-O1 --skip-build --root=%{buildroot} --prefix=%{_prefix}"
#	DESTDIR="%{buildroot}" \
#	PREFIX="%{buildroot}%{python_libdir}" \
#	PYLIBDIR="%{buildroot}%{python_libdir}"
#	PYLIBDIR="%{buildroot}%{python_sitearch}"
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CREDITS LICENSE README TODO
%doc %{_mandir}/man1/makeswf*
%{_bindir}/dbl2png
%{_bindir}/gif2dbl
%{_bindir}/gif2mask
%{_bindir}/listaction_d
%{_bindir}/listswf_d
%{_bindir}/makeswf
%{_bindir}/ming-config
%{_bindir}/png2dbl
%{_bindir}/png2swf
%{_bindir}/raw2adpcm
%{_bindir}/swftoperl
%{_bindir}/swftopython
%{_bindir}/listaction
%{_bindir}/listfdb
%{_bindir}/listjpeg
%{_bindir}/listmp3
%{_bindir}/listswf
%{_bindir}/makefdb
%{_bindir}/swftophp
%{_libdir}/libming.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/ming.h
%{_includedir}/ming_config.h
%{_includedir}/mingpp.h
%{_libdir}/libming.a
%{_libdir}/libming.so

%files -n perl-ming
%defattr(-, root, root, 0755)
%doc perl_ext/README perl_ext/TODO
%doc %{_mandir}/man3/SWF*
%{perl_vendorarch}/SWF.pm
%{perl_vendorarch}/SWF/
%{perl_vendorarch}/auto/SWF/

%if %{!?_without_python:1}0
%files -n python-ming
%defattr(-, root, root, 0755)
%doc py_ext/README py_ext/TODO
%{python_sitearch}/_mingc.so
%{python_sitearch}/ming.py
%{python_sitearch}/ming.pyc
%ghost %{python_sitearch}/ming.pyo
%{python_sitearch}/mingc.py
%{python_sitearch}/mingc.pyc
%ghost %{python_sitearch}/mingc.pyo
%endif

%changelog
* Sat Oct 14 2006 Dag Wieers <dag@wieers.com> - 0.3.0-3
- Fixed group name.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 0.3.0-2
- Added perl and python bindings.

* Sun May 28 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.0-1
- Updated to release 0.3.0.
- Bindings (ming-perl, ming-php, ..) are distributed in separate files now.

* Tue Mar 15 2005 Dag Wieers <dag@wieers.com> - 0.2a-2
- Made libming libraries executable.

* Fri May 14 2004 Dag Wieers <dag@wieers.com> - 0.2a-1
- Initial package. (using DAR)
