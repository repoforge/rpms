# $Id: _template.spec 219 2004-04-09 06:21:45Z dag $
# Authority: dag
# Upstream: <clearsilver@neotonic.com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define need_buildroot %(perl -e 'use ExtUtils::MakeMaker; print ($ExtUtils::MakeMaker::VERSION<6.10?1:0)')

Summary: ClearSilver HTML template system
Name: clearsilver
Version: 0.9.8
Release: 1
License: Apache License style
Group: Development/Libraries
URL: http://www.clearsilver.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.clearsilver.net/downloads/clearsilver-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, python-devel
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

### If older ExtUtils-MakeMaker, set DESTDIR
%if "%{need_buildroot}" == "1"
%{?need_buildroot:%{__perl} -pi.orig -e 's|^(WriteMakefile\()$|$1\n\t"PREFIX"\t=>\t"%{buildroot}%{_prefix}",|' perl/Makefile.PL}
%endif
%{__perl} -pi.orig -e 's|/usr/local|%{_prefix}|' scripts/document.py

%build
%configure \
	--enable-apache \
	--enable-java \
	--enable-python \
	--enable-perl \
	--disable-csharp \
	--disable-ruby

#%{__perl} -pi.orig -e '
#		s|^(PYTHON)\s*=.*$|$1=python|;
#		s|^(DESTDIR)\s*=.*$|$1=%{buildroot}|;
#	' rules.mk
#		s|^(PYTHON_SITE)\s*=.*$|$1=lib/python%pyver/ |;

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}" \
	INSTALLDIRS="vendor"
%{__make} install -C python \
	DESTDIR="%{buildroot}"
%{__make} install -C perl \
	DESTDIR="%{buildroot}" \
	INSTALLDIRS="vendor"

### Clean up buildroot (arch)
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc CS_LICENSE INSTALL LICENSE README scripts/cs_lint.py contrib/cs-mode.el 
%doc %{_mandir}/man3/*.3.*
%{_bindir}/*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/ClearSilver/
%{_libdir}/*.a

%files -n python-clearsilver
%defattr(-, root, root, 0755)
%doc README.python
%{_libdir}/python*/site-packages/neo_cgi.so

%files -n perl-ClearSilver
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/ClearSilver.pm
%{perl_vendorarch}/auto/ClearSilver/ClearSilver.so
%{perl_vendorarch}/auto/ClearSilver/ClearSilver.bs

#%files -n ruby
#%defattr(-, root, root, 0755)
#{ruby_sitepath}/(ruby_version}/neo.rb
#{ruby_sitepath}/(ruby_version}/$(ruby_arch}/hdf.so

#%files -n mod_ecs
#{apache_libexec}/mod_ecs.so

%changelog
* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 0.9.8-1
- Initial package. (using DAR)
