# $Id$
# Authority: dries
# Upstream: Jesse Vincent <jesse$bestpractical,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-ICal

Summary: Generates iCalendar (RFC 2445) calendar files
Name: perl-Data-ICal
Version: 0.16
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-ICal/

Source: http://search.cpan.org/CPAN/authors/id/A/AL/ALEXMV/Data-ICal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Class::ReturnValue)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MIME::QuotedPrint)
BuildRequires: perl(Test::LongString)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(Text::vFile::asData)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Class::Accessor)
Requires: perl(Class::ReturnValue)
Requires: perl(MIME::QuotedPrint)
Requires: perl(Text::vFile::asData)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
A Data::ICal object represents a VCALENDAR  object as defined in the iCalendar
protocol (RFC 2445, MIME type "text/calendar"), as implemented in many popular
calendaring programs such as Apple's iCal.

Each Data::ICal object is a collection of "entries", which are objects of a
subclass of Data::ICal::Entry. The types of entries defined by iCalendar (which
refers to them as "components") include events, to-do items, journal entries,
free/busy time indicators, and time zone descriptors; in addition, events and
to-do items can contain alarm entries. (Currently, Data::ICal only implements
to-do items and events.)

Data::ICal is a subclass of Data::ICal::Entry; see its manpage for more methods
applicable to Data::ICal.

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
%doc Changes META.yml README SIGNATURE
%doc doc/ examples/
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Data/ICal.pm
%{perl_vendorlib}/Data/ICal/*
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Wed Jul 28 2010 Steve Huff <shuff@vecna.org> - 0.16
- Initial package.
