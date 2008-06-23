# $Id$
# Authority: dries
# Upstream: Allen Day <allenday$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Widget

Summary: Create common page elements
Name: perl-CGI-Widget
Version: 0.15
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Widget/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Widget-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Modules under the CGI::Widget namespace serve the purpose of allowing
authors of CGI or other dynamically generated HTML documents an easy way
to create common, although perhaps complex, page elements.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/CGI/Widget.pm
%{perl_vendorlib}/CGI/Widget

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Initial package.
