# $Id$
# Authority: dries
# Upstream: Sanford Morton <smorton$pobox,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chart-Plot

Summary: Plot two dimensional data in an image
Name: perl-Chart-Plot
Version: 0.11
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Chart-Plot/

Source: http://search.cpan.org/CPAN/authors/id/S/SM/SMORTON/Chart-Plot-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Chart::Plot will plot multiple data sets in the same graph, each with
negative or positive values in the independent or dependent
variables. Each dataset can be a scatter graph (data are represented
by graph points only) or with lines connecting successive data points,
or both. Colors and dashed lines are supported, as is scientific
notation (1.7E10). Axes are scaled and positioned automatically and
5-10 ticks are drawn and labeled on each axis.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Chart/Plot.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.11-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Initial package.
