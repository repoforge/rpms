# $Id$
# Authority: dries
# Upstream: Jim Thomason <jim$jimandkoka,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-Bulkmail

Summary: Platform independent mailing list module
Name: perl-Mail-Bulkmail
Version: 3.12
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-Bulkmail/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-Bulkmail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Platform independent mailing list module.

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
%doc Changes
%doc %{_mandir}/man3/Mail::Bulkmail*
%{perl_vendorlib}/Mail/Bulkmail.pm
%{perl_vendorlib}/Mail/Bulkmail/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 3.12-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 3.12-1
- Initial package.
