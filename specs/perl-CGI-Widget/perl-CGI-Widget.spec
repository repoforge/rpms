# $Id$
# Authority: dries
# Upstream: Allen Day <allenday$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Widget

Summary: Create common page elements
Name: perl-CGI-Widget
Version: 0.15
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Widget/

Source: http://search.cpan.org/CPAN/authors/id/A/AL/ALLENDAY/CGI-Widget-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

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
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/CGI/Widget.pm
%{perl_vendorlib}/CGI/Widget

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.15-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Initial package.

