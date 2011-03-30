# $Id$
# Authority: shuff
# Upstream: Robert Krimen <robertkrimen$gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Google-Search

Summary: Interface to the Google AJAX Search API and suggestion API
Name: perl-Google-Search
Version: 0.027
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Google-Search/

Source: http://search.cpan.org/CPAN/authors/id/R/RO/ROKR/Google-Search-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Any::Moose)
BuildRequires: perl(Carp::Clan::Share)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(JSON) >= 2
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Try::Tiny)
BuildRequires: perl(URI)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Any::Moose)
Requires: perl(Carp::Clan::Share)
Requires: perl(JSON) >= 2
Requires: perl(LWP::UserAgent)
Requires: perl(Try::Tiny)
Requires: perl(URI)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Google::Search is an interface to the Google AJAX Search API
(http://code.google.com/apis/ajaxsearch/).

Currently, their API looks like it will fetch you the top 64 results for your
search query.

You may want to sign up for an API key, but it is not required. You can do so
here: http://code.google.com/apis/ajaxsearch/signup.html

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\\.31.*/ && s/6\\.3\\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Google/Search.pm
%{perl_vendorlib}/Google/Search/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Wed Mar 30 2011 Steve Huff <shuff@vecna.org> - 0.027-1
- Initial package.
