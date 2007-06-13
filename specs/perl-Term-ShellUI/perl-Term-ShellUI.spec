# $Id$
# Authority: dries
# Upstream: Scott Bronson <bronson$rinspin,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Term-ShellUI

Summary: A fully-featured shell-like command line environment
Name: perl-Term-ShellUI
Version: 0.86
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Term-ShellUI/

Source: http://search.cpan.org//CPAN/authors/id/B/BR/BRONSON/Term-ShellUI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
A fully-featured shell-like command line environment.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

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
