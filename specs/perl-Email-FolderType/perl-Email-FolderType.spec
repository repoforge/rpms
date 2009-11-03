# $Id$
# Authority: dag
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-FolderType

Summary: Determine the type of a mail folder
Name: perl-Email-FolderType
Version: 0.813
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-FolderType/

Source: http://www.cpan.org/modules/by-module/Email/Email-FolderType-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Determine the type of a mail folder.

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
%doc Changes LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Email::FolderType.3pm*
%doc %{_mandir}/man3/Email::FolderType::*.3pm*
%dir %{perl_vendorlib}/Email/
%{perl_vendorlib}/Email/FolderType/
%{perl_vendorlib}/Email/FolderType.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.813-1
- Initial package. (using DAR)
