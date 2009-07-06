# $Id$
# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-MessageID

Summary: Generate world unique message-ids
Name: perl-Email-MessageID
Version: 1.401
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-MessageID/

Source: http://www.cpan.org/modules/by-module/Email/Email-MessageID-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Message-ids are optional, but highly recommended, headers that identify
a message uniquely. This software generates a unique message-id. This
module generates world unique message-ids.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Email::MessageID.3pm*
%dir %{perl_vendorlib}/Email/
#%{perl_vendorlib}/Email/MessageID/
%{perl_vendorlib}/Email/MessageID.pm

%changelog
* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 1.401-1
- Updated to version 1.401.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.400-1
- Updated to release 1.400.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.351-1
- Updated to release 1.351.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.35-1
- Updated to release 1.35.

* Sun Jan  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.31-1
- Initial package.
