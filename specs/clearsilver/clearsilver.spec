# $Id$
# Authority: dag
# Upstream: <clearsilver$neotonic,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define need_buildroot %(perl -e 'use ExtUtils::MakeMaker; print ($ExtUtils::MakeMaker::VERSION<6.10?1:0)')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: ClearSilver HTML template system
Name: clearsilver
Version: 0.10.4
Release: 2%{?dist}
License: Apache License style
Group: Development/Libraries
URL: http://www.clearsilver.net/

Source: http://www.clearsilver.net/downloads/clearsilver-%{version}.tar.gz
Patch0: clearsilver-0.10.3-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, python-devel, python, perl(ExtUtils::MakeMaker)
#BuildRequires: perl-devel, ruby >= 1.4.5

%description
ClearSilver is a fast, powerful, and language-neutral HTML template system.
In both static content sites and dynamic HTML applications, it provides a
separation between presentation code and application logic which makes
working with your project easier.

%package devel
Summary: ClearSilver development package
Group: Development/Libraries

%description devel
This package provides needed files to develop extension
to ClearSilver.

%package -n python-clearsilver
Summary: Neotonic ClearSilver Python Module
Group: Development/Libraries
Requires: clearsilver = %{version}

%description -n python-clearsilver
This package provides a python interface to the
clearsilver CGI kit and templating system.

%package -n perl-ClearSilver
Summary: Neotonic ClearSilver Perl Module
Group: Development/Libraries
Requires: clearsilver = %{version}
Obsoletes: perl-clearsilver <= %{version}-%{release}
Provides: perl-clearsilver = %{version}-%{release}

%description -n perl-ClearSilver
The clearsilver-perl package provides a perl interface to the
clearsilver templating system.

%package -n ruby-clearsilver
Summary: Neotonic ClearSilver Ruby Module
Group: Development/Libraries
Requires: clearsilver = %version

%description -n ruby-clearsilver
The clearsilver-ruby package provides a ruby interface to the
clearsilver templating system.

%prep
%setup
%patch0 -p1

%{__perl} -pi -e 's|/neo/opt/bin/python|%{__python}|' python/examples/*/*.py
find python/examples -type f | xargs chmod -x

%build
%configure \
	--with-python="%{__python}" \
	--enable-apache \
	--enable-java \
	--enable-python \
	--enable-perl \
	--disable-csharp \
	--disable-ruby

cd perl
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
cd -
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall PYTHON_SITE="%{buildroot}%{python_sitearch}"

### Clean up buildroot (arch)
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc contrib/cs-mode.el CS_LICENSE INSTALL LICENSE README scripts/cs_lint.py
%doc %{_mandir}/man3/*.3.*
%{_bindir}/*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/ClearSilver/
%{_libdir}/libneo_*.a

%files -n python-clearsilver
%defattr(-, root, root, 0755)
%doc README.python
%{_libdir}/python*/site-packages/neo_cgi.so

%files -n perl-ClearSilver
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/ClearSilver.pm
%{perl_vendorarch}/auto/ClearSilver/

#%files -n ruby
#%defattr(-, root, root, 0755)
#{ruby_sitepath}/(ruby_version}/neo.rb
#{ruby_sitepath}/(ruby_version}/$(ruby_arch}/hdf.so

#%files -n mod_ecs
#{apache_libexec}/mod_ecs.so

%changelog
* Thu Apr 19 2007 Dries Verachtert <dries@ulyssis.org> - 0.10.4-2
- Make SPEC file work on EL3 and older.

* Wed Apr 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.10.4-1
- Updated to release 0.10.4.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.10.2-1
- Updated to release 0.10.2.

* Sat Nov 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.10.1-1
- Updated to release 0.10.1.

* Mon Nov 29 2004 Dag Wieers <dag@wieers.com> - 0.9.13-1
- Updated to release 0.9.13.

* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 0.9.8-1
- Initial package. (using DAR)
