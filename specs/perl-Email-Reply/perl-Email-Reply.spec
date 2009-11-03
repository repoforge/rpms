# $Id$
# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Reply

Summary: Reply to mails
Name: perl-Email-Reply
Version: 1.202
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Reply/

Source: http://www.cpan.org/modules/by-module/Email/Email-Reply-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl package to reply to mails.

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
%doc %{_mandir}/man3/Email::Reply.3pm*
%dir %{perl_vendorlib}/Email/
#%{perl_vendorlib}/Email/Reply/
%{perl_vendorlib}/Email/Reply.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.202-1
- Updated to release 1.202.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.201-1
- Updated to release 1.201.

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 1.200-1
- Initial package.
