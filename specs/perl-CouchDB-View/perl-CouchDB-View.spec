# $Id$
# Authority: shuff
# Upstream: Hans Dieter Pearcey <hdp$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CouchDB-View

Summary: handle and create CouchDB views in Perl
Name: perl-CouchDB-View
Version: 0.003
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CouchDB-View/

Source: http://search.cpan.org/CPAN/authors/id/H/HD/HDP/CouchDB-View-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Data::Dump::Streamer)
BuildRequires: perl(JSON::XS)
BuildRequires: perl(PadWalker)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI::Escape)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Data::Dump::Streamer)
Requires: perl(JSON::XS)
Requires: perl(PadWalker)
Requires: perl(URI::Escape)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
CouchDB::View::Document provides a Perlish interface to creating CouchDB views.
It uses Data::Dump::Streamer to serialize coderefs, which are deserialized and
used by CouchDB::View::Server.

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
%{_bindir}/*
%{perl_vendorlib}/CouchDB/View.pm
%{perl_vendorlib}/CouchDB/View/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri Sep 24 2010 Steve Huff <shuff@vecna.org> - 0.003-1
- Initial package.
