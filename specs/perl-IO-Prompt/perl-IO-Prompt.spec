# $Id$
# Authority: dag
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Prompt

Summary: Perl module to interactively prompt for user input.
Name: perl-IO-Prompt
Version: 0.996
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Prompt/

Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCONWAY/IO-Prompt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(POSIX)
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(Test::More)
BuildRequires: perl(Want)
BuildRequires: perl(version)
Requires: perl(IO::Handle)
Requires: perl(POSIX)
Requires: perl(Term::ReadKey)
Requires: perl(Test::More)
Requires: perl(Want)
Requires: perl(version)

%filter_from_requires /^perl*/d
%filter_setup

%description
IO-Prompt is a Perl module to interactively prompt for user input.

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
%doc %{_mandir}/man3/IO::Prompt.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/IO/
#%{perl_vendorlib}/IO/Prompt/
%{perl_vendorlib}/IO/Prompt.pm

%changelog
* Tue Jan 12 2010 Christoph Maser <cmr@financial.com> - 0.996-1
- Updated to version 0.996.

* Thu May 31 2007 Dag Wieers <dag@wieers.com> - 0.99.4-1
- Initial package. (using DAR)
