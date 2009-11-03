# $Id$
# Authority: dries
# Upstream: Stephen Farrell <steve$farrell,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-TableLayout

Summary: Layout Manager for cgi-based web applications
Name: perl-HTML-TableLayout
Version: 1.001008
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-TableLayout/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-TableLayout-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Layout Manager for cgi-based web applications.

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
%doc README RELEASE_NOTES
%doc %{_mandir}/man3/*
%{perl_vendorlib}/HTML/TableLayout.pm
%{perl_vendorlib}/HTML/TableLayout

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.001008-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.001008-1
- Initial package.
