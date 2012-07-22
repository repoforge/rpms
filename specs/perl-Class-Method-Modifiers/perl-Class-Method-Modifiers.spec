# $Id$
# Authority: dfateyev
# Upstream: Shawn M Moore <sartak$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Method-Modifiers

Summary: Provides Moose-like method modifiers
Name: perl-%{real_name}
Version: 1.09
Release: 1%{?dist}
License: GPL or Artistic
Group: Development/Libraries
URL: http://github.com/sartak/Class-Method-Modifiers/tree

Source0: http://search.cpan.org/CPAN/authors/id/S/SA/SARTAK/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Class::Method::Modifiers provides three modifiers: before, around, and
after.  In short, Class::Method::Modifiers solves the problem of making
sure you call $self->SUPER::foo(@_), and provides a cleaner interface
for it.

%prep
%setup -n %{real_name}-%{version}
echo "Generic README file for %{real_name}" > README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} pure_install
find %{buildroot} -type f -name .packlist -exec %{__rm} -f {} ';'
find %{buildroot} -type f -name *.bs -exec %{__rm} -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc Changes README
%{perl_vendorlib}/Class/Method/Modifiers.pm
%{_mandir}/man3/*.3*

%changelog
* Sat Apr 28 2012 Denis Fateyev <denis@fateyev.com> - 1.09-1
- Initial package.
