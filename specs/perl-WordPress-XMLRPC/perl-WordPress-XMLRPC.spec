# $Id$
# Authority: dfateyev
# Upstream: Leo Charre <leocharre$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WordPress-XMLRPC

Summary: WordPress-XMLRPC perl module
Name: perl-WordPress-XMLRPC
Version: 1.23
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WordPress-XMLRPC/

Source: http://search.cpan.org/CPAN/authors/id/L/LE/LEOCHARRE/WordPress-XMLRPC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl(LEOCHARRE::CLI2)
Requires: perl(LEOCHARRE::Debug)
Requires: perl(Smart::Comments)
Requires: perl(SOAP::Lite)
Requires: perl(XMLRPC::Lite)
Requires: perl(YAML)
Requires: perl(ExtUtils::MakeMaker)
# BuildRequires: rpm-macros-rpmforge

### Remove autoreq Perl dependencies
# %filter_from_requires /^perl.*/d
# %filter_setup

%description
WordPress-XMLRPC perl module

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
# $Id$
# Authority: dfateyev
# Upstream: Leo Charre <leocharre$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WordPress-XMLRPC

Summary: WordPress-XMLRPC perl module
Name: perl-WordPress-XMLRPC
Version: 1.23
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WordPress-XMLRPC/

Source: http://search.cpan.org/CPAN/authors/id/L/LE/LEOCHARRE/WordPress-XMLRPC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl(LEOCHARRE::CLI2)
Requires: perl(LEOCHARRE::Debug)
Requires: perl(Smart::Comments)
Requires: perl(SOAP::Lite)
Requires: perl(XMLRPC::Lite)
Requires: perl(YAML)
Requires: perl(ExtUtils::MakeMaker)
# BuildRequires: rpm-macros-rpmforge

### Remove autoreq Perl dependencies
# %filter_from_requires /^perl.*/d
# %filter_setup

%description
WordPress-XMLRPC perl module

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/WordPress/

%changelog
* Mon May 23 2011 Denis Fateyev <denis@fateyev.com> - 1.23-1
- Initial package.

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/WordPress/

%changelog
* Mon May 23 2011 Denis Fateyev <denis@fateyev.com> - 1.23-1
- Initial package.

