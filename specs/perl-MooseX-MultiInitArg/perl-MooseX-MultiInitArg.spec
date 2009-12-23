# $Id$
# Authority: shuff
# Upstream: Paul Driver <frodwith$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-MultiInitArg

Summary: Attributes with aliases for constructor arguments
Name: perl-%{real_name}
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-MultiInitArg/

Source: http://search.cpan.org/CPAN/authors/id/F/FR/FRODWITH/MooseX-MultiInitArg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Moose)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
If you've ever wanted to be able to call an attribute any number of things
while you're passing arguments to your object constructor, Now You Can.

The primary motivator is that I have some attributes that were named
inconsistently, and I wanted to rename them without breaking backwards
compatibility with my existing API.

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
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/MooseX/
%{perl_vendorlib}/MooseX/*

%changelog
* Wed Dec 23 2009 Steve Huff <shuff@vecna.org> - 0.01-1
- Initial package.
