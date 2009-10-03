# $Id$
# Authority: shuff
# Upstream: James Tolley <james$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Email

Summary: Test Email Contents
Name: perl-%{real_name}
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Email/

Source: http://search.cpan.org/CPAN/authors/id/J/JA/JAMES/Test-Email-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Mail::POP3Client) >= 2
BuildRequires: perl(Mail::Sendmail) >= 0.79
BuildRequires: perl(MIME::Entity) >= 5.4
BuildRequires: perl(MIME::Parser) >= 5.4
# Seems to build OK with the stock RHEL5 Test::Builder
#BuildRequires: perl(Test::Builder) >= 0.7

%description
Please note that this is ALPHA CODE. As such, the interface is likely to
change.

Test::Email is a subclass of MIME::Entity, with the above methods. If you want
the messages fetched from a POP3 account, use Test::POP3.

Tests for equality remove trailing newlines from strings before testing. This
is because some mail messages have newlines appended to them during the mailing
process, which could cause unnecessary confusion.

This module should be 100% self-explanatory. If not, then please look at
Test::Simple and Test::More for clarification.


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
%doc README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Email.pm
%{perl_vendorlib}/Test/POP3.pm

%changelog
* Sat Oct 03 2009 Steve Huff <shuff@vecna.org> - 0.07-1
- Initial package.
