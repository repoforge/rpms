# $Id$
# Authority: dag
# Upstream: John Kirk <johnkirk$dystanhays,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-TreeFile

Summary: Reads a tree of text strings into a data structure
Name: perl-Text-TreeFile
Version: 0.39
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-TreeFile/

Source: http://www.cpan.org/modules/by-module/Text/Text-TreeFile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Reads a tree of text strings into a data structure.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Text::TreeFile.3pm*
%doc %{_mandir}/man3/Text::TreeFile::*.3pm*
%dir %{perl_vendorlib}/auto/Text/
%{perl_vendorlib}/auto/Text/TreeFile/
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/TreeFile/
%{perl_vendorlib}/Text/TreeFile.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.39-1
- Initial package. (using DAR)
