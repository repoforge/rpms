# $Id$
# Authority: dag
# Upstream: Mark Overmeer <mark$overmeer,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Hash-Case

Summary: Perl module that implements a base class for hashes with key-casing requirements
Name: perl-Hash-Case
Version: 1.006
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Hash-Case/

Source: http://www.cpan.org/modules/by-module/Hash/Hash-Case-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Hash-Case is a Perl module that implements a base class for hashes
with key-casing requirements.

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
%{__rm} -f %{buildroot}%{perl_vendorlib}/Hash/Makefile.PL

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/Hash::Case.3pm*
%doc %{_mandir}/man3/Hash::Case::*.3pm*
%dir %{perl_vendorlib}/Hash/
%{perl_vendorlib}/Hash/Case/
%{perl_vendorlib}/Hash/Case.pm
%{perl_vendorlib}/Hash/Case.pod

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.006-1
- Updated to release 1.006.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 1.004-1
- Initial package. (using DAR)
