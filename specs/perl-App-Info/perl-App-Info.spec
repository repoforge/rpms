# $Id$
# Authority: dries
# Upstream: David Wheeler <david$justatheory,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name App-Info

Summary: Provides metadata about installed software packages
Name: perl-App-Info
Version: 0.51
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/App-Info/

Source: http://search.cpan.org/CPAN/authors/id/D/DW/DWHEELER/App-Info-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Module-Build

%description
App::Info provides a generalized interface for providing metadata about
software packages installed on a system. The idea is that App::Info subclasses
can be used in Perl application installers in order to determine whether
software dependencies have been fulfilled, and to get necessary metadata about
those software packages.

App::Info provides an event model for handling events triggered by App::Info
subclasses. The events are classified as "info", "error", "unknown", and
"confirm" events, and multiple handlers may be specified to handle any or all
of these event types. This allows App::Info clients to flexibly handle events
in any way they deem necessary. Implementing new event handlers is
straight-forward, and use the triggering of events by App::Info subclasses is
likewise kept easy-to-use.

A few sample App::Info and App::Info::Handler (event handling) subclasses are
provided with the distribution, but others are invited to write their own
subclasses and contribute them to the CPAN. Contributors are welcome to extend
their subclasses to provide more information relevant to the application for
which data is to be provided (see App::Info::HTTPD::Apache for an example),
but are encouraged to, at a minimum, implement the methods defined by the
App::Info abstract base class relevant to the category of software they're
managing, e.g. App::Info::HTTPD or App::Info::RDBMS. New categories will be
added as needed.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/App/Info.pm
%{perl_vendorlib}/App/Info/

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.51-1
- Updated to release 0.51.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.50-1
- Updated to release 0.50.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.49-1
- Updated to release 0.49.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.48-1
- Updated to release 0.48.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.47-1
- Initial package.

