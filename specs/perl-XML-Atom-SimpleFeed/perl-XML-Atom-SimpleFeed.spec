# $Id$
# Authority: shuff
# Upstream: Aristotle Pagaltzis <pagaltzis$gmx,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Atom-SimpleFeed

Summary: No-fuss generation of Atom syndication feeds
Name: perl-XML-Atom-SimpleFeed
Version: 0.86
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Atom-SimpleFeed/

Source: http://search.cpan.org/CPAN/authors/id/A/AR/ARISTOTLE/XML-Atom-SimpleFeed-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8.1
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.1

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module provides a minimal API for generating Atom syndication feeds
quickly and easily. It supports all aspects of the Atom format, but has no
provisions for generating feeds with extension elements.

You can supply strings for most things, and the module will provide useful
defaults. When you want more control, you can provide data structures, as
documented, to specify more particulars.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/XML/Atom/SimpleFeed.pm
#%{perl_vendorlib}/XML/Atom/SimpleFeed/*
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Tue Aug 03 2010 Steve Huff <shuff@vecna.org> - 0.86-1
- Initial package.
