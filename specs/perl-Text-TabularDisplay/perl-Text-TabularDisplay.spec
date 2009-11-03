# $Id$
# Authority: dag
# Upstream: Darren Chamberlain <darren$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-TabularDisplay

Summary: Perl module to display text in formatted table output
Name: perl-Text-TabularDisplay
Version: 1.22
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-TabularDisplay/

Source: http://www.cpan.org/modules/by-module/Text/Text-TabularDisplay-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Text-TabularDisplay is a Perl module to display text
in formatted table output.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Text::TabularDisplay.3pm*
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/TabularDisplay.pm

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 1.22-1
- Initial package. (using DAR)
