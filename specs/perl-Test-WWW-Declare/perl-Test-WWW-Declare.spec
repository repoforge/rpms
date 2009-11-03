# $Id$
# Authority: shuff
# Upstream: Shawn M Moore <sartak$bestpractical,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-WWW-Declare

Summary: declarative testing for your web app
Name: perl-%{real_name}
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-WWW-Declare/

Source: http://search.cpan.org/CPAN/authors/id/S/SA/SARTAK/Test-WWW-Declare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTTP::Server::Simple) >= 0.35
BuildRequires: perl(Test::Tester) >= 0.107

%description
Often in web apps, tests are very dependent on the state set up by previous
tests. If one test fails (e.g. "follow the link to the admin page") then it's
likely there will be many more failures. This module aims to alleviate this
problem, as well as provide a nicer interface to Test::WWW::Mechanize.

The central idea is that of "flow". Each flow is a sequence of commands ("fill
in this form") and assertions ("content should contain 'testuser'"). If any of
these commands or assertions fail then the flow is aborted. Only that one
failure is reported to the test harness and user. Flows may also contain other
flows. If an inner flow fails, then the outer flow fails as well.



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
%doc Changes SIGNATURE MANIFEST doc/
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Test/WWW/Declare
%{perl_vendorlib}/Test/WWW/Declare.pm
%{perl_vendorlib}/Test/WWW/Declare/Tester.pm

%changelog
* Sat Oct 03 2009 Steve Huff <shuff@vecna.org> - 0.07-1
- Initial package.
