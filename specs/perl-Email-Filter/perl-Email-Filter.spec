# $Id$
# Authority: shuff
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Filter

Summary: Library for creating easy email filters
Name: perl-Email-Filter
Version: 1.032
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Filter/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Email-Filter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Class::Trigger) >= 0.08
BuildRequires: perl(Email::LocalDelivery) >= 0.07
BuildRequires: perl(Email::Simple) >= 1.91
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IPC::Run) >= 0.77
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: rpm-macros-rpmforge
Requires: perl(Class::Trigger) >= 0.08
Requires: perl(Email::LocalDelivery) >= 0.07
Requires: perl(Email::Simple) >= 1.91
Requires: perl(IPC::Run) >= 0.77

### remove autoreq Perl dependencies
%filter_from_requires /^perl*/d
%filter_setup


%description
This is another module produced by the "Perl Email Project", a reaction against
the complexity and increasing bugginess of the "Mail::*" modules. It replaces
Mail::Audit, and allows you to write programs describing how your mail should
be filtered.

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
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Email/
%{perl_vendorlib}/Email/Filter.pm

%changelog
* Tue Apr 06 2010 Steve Huff <shuff@vecna.org> - 1.032-1
- Initial package.
