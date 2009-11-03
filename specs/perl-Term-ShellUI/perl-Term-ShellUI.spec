# $Id$
# Authority: dries
# Upstream: Scott Bronson <bronson$rinspin,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Term-ShellUI

Summary: A fully-featured shell-like command line environment
Name: perl-Term-ShellUI
Version: 0.86
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Term-ShellUI/

Source: http://www.cpan.org/modules/by-module/Term/Term-ShellUI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A fully-featured shell-like command line environment.

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
%doc %{_mandir}/man3/Term::ShellUI*
%doc %{_mandir}/man3/Text::Shellwords::Cursor*
%{perl_vendorlib}/Term/ShellUI.pm
%{perl_vendorlib}/Text/Shellwords/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.86-1
- Initial package.
