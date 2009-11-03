# $Id$
# Authority: dag
# Upstream: David Glasser <glasser@bestpractical.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Tags

Summary: Parses "folksonomy" space-separated tags (stub module)
Name: perl-Text-Tags
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Tags/

Source: http://www.cpan.org/modules/by-module/Text/Text-Tags-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Parses "folksonomy" space-separated tags (stub module).

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
%doc %{_mandir}/man3/Text::Tags.3pm*
%doc %{_mandir}/man3/Text::Tags::Parser.3pm*
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/Tags/
%{perl_vendorlib}/Text/Tags.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
