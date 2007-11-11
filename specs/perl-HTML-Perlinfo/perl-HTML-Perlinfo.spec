# $Id$
# Authority: dries
# Upstream: Michael Accardo <mikeaccardo$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Perlinfo

Summary: Display a lot of Perl information in HTML format
Name: perl-HTML-Perlinfo
Version: 1.47
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Perlinfo/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Perlinfo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Display a lot of Perl information in HTML format.

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
%doc %{_mandir}/man3/HTML::Perlinfo*
%{perl_vendorlib}/HTML/Perlinfo.pm
%{perl_vendorlib}/HTML/Perlinfo/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.47-1
- Initial package.
