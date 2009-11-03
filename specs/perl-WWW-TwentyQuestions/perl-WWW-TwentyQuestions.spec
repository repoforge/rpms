# $Id$
# Authority: dries
# Upstream: Casey Kirsle <kirsle$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-TwentyQuestions

Summary: Interface to the classic 20 Questions game as provided by 20Q.net
Name: perl-WWW-TwentyQuestions
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-TwentyQuestions/

Source: http://search.cpan.org//CPAN/authors/id/K/KI/KIRSLE/WWW-TwentyQuestions-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 4:5.8.8
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 4:5.8.8

%description
Interface to the classic 20 Questions game as provided by 20Q.net.

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
%doc %{_mandir}/man3/WWW::TwentyQuestions*
%{perl_vendorlib}/WWW/TwentyQuestions.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
