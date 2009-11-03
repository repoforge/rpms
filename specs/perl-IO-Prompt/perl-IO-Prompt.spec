# $Id$
# Authority: dag
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Prompt
%define real_version 0.099004

Summary: Perl module to interactively prompt for user input.
Name: perl-IO-Prompt
Version: 0.99.4
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Prompt/

Source: http://www.cpan.org/modules/by-module/IO/IO-Prompt-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
IO-Prompt is a Perl module to interactively prompt for user input.

%prep
%setup -n %{real_name}-v%{version}

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
* Thu May 31 2007 Dag Wieers <dag@wieers.com> - 0.99.4-1
- Initial package. (using DAR)
