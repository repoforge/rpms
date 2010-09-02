# $Id$
# Authority: dag
# Upstream: Joe Schaefer <joe+cpan$sunstarsys,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name libapreq2

Summary: Wrapper for libapreq2's module/handle API
Name: perl-libapreq2
Version: 2.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/libapreq2/

Source: http://www.cpan.org/authors/id/J/JO/JOESUF/libapreq2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: apr-devel
BuildRequires: apr-util-devel
BuildRequires: httpd-devel
BuildRequires: mod_perl-devel
BuildRequires: perl >= 1:5.6.1
BuildRequires: perl(Apache::Test) >= 1.04
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.15
BuildRequires: perl(ExtUtils::XSBuilder) >= 0.23
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(mod_perl2) >= 1.999022
Requires: perl(mod_perl2) >= 1.999022
Requires: perl >= 1:5.6.1

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Wrapper for libapreq2's module/handle API.

%package -n libapreq2
Summary: Apache HTTP request library
Group: System Environment/Libraries

Requires: /sbin/ldconfig
Provides: libapreq = %{version}-%{release}
Obsoletes: libapreq <= %{version}-%{release}

%description -n libapreq2
libapreq is a shared library with associated modules for manipulating
client request data via the Apache API.  Functionality includes
parsing of application/x-www-form-urlencoded and multipart/form-data
content, as well as HTTP cookies.

%package -n libapreq2-devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries

Requires: %{name} = %{version}-%{release}
Requires: httpd-devel >= 2.0.48
Requires: pkgconfig
Provides: libapreq-devel = %{version}-%{release}
Obsoletes: libapreq-devel <= %{version}-%{release}

%description -n libapreq2-devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
    --disable-dependency-tracking \
    --disable-static \
    --enable-perl-glue \
    --with-mm-opts="INSTALLDIRS=vendor"
#    --with-apache2-apxs="%{apxs}" \
#CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%post -n libapreq2 -p /sbin/ldconfig
%postun -n libapreq2 -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES FAQ.pod INSTALL LICENSE MANIFEST META.yml NOTICE README 
%doc %{_mandir}/man3/Apache2::Cookie.3pm*
%{_mandir}/man3/APR::Request.3pm.gz
%{_mandir}/man3/APR::Request::Apache2.3pm.gz
%{_mandir}/man3/APR::Request::CGI.3pm.gz
%{_mandir}/man3/APR::Request::Cookie.3pm.gz
%{_mandir}/man3/APR::Request::Error.3pm.gz
%{_mandir}/man3/APR::Request::Hook.3pm.gz
%{_mandir}/man3/APR::Request::Param.3pm.gz
%{_mandir}/man3/APR::Request::Parser.3pm.gz
%{_mandir}/man3/Apache2::Request.3pm.gz
%{_mandir}/man3/Apache2::Upload.3pm.gz
%{_bindir}/apreq2-config
%{_includedir}/httpd/apreq2/apreq_module_apache2.h
%{_includedir}/apreq2/apreq.h
%{_includedir}/apreq2/apreq_cookie.h
%{_includedir}/apreq2/apreq_error.h
%{_includedir}/apreq2/apreq_module.h
%{_includedir}/apreq2/apreq_param.h
%{_includedir}/apreq2/apreq_parser.h
%{_includedir}/apreq2/apreq_util.h
%{_includedir}/apreq2/apreq_version.h
%{_libdir}/httpd/modules/mod_apreq2.la
%{_libdir}/httpd/modules/mod_apreq2.so
%{_libdir}/libapreq2.la
%{_libdir}/libapreq2.so*
%{perl_vendorarch}/APR
%{perl_vendorarch}/Apache2
%{perl_vendorarch}/auto/libapreq2/
%{perl_vendorarch}/auto/APR
%exclude %{perl_archlib}/perllocal.pod

%changelog
* Fri Sep  3 2010 Christoph Maser <cmr@financial.com> - 2.12-1
- Updated to version 2.12.
- Add BuildRequires: mod_perl-devel
- Change build from perl module style to autotools project style
- Update %files section

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 2.08-1
- Initial package. (using DAR)
