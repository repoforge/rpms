# $Id$
# Authority: dag
# Upstream: Laurent Dami <laurent,dami$etat,ge,ch>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Hash-Type

Summary: pseudo-hashes as arrays tied to a "type" (list of fields)
Name: perl-Hash-Type
Version: 1.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Hash-Type/

Source: http://www.cpan.org/modules/by-module/Hash/Hash-Type-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Hash-Type is a Perl module that implements pseudo-hashes as arrays
tied to a "type" (list of fields).

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
%doc %{_mandir}/man3/Hash::Type.3pm*
%dir %{perl_vendorlib}/Hash/
%{perl_vendorlib}/Hash/Type.pm

%changelog
* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 1.08-1
- Updated to release 1.08.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.05-1
- Initial package. (using DAR)
