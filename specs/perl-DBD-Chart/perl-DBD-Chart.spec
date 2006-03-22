# $Id$
# Authority: dries
# Upstream: Dean Arnold <darnold$presicient,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-Chart

Summary: DBI driver abstraction for Rendering Charts and Graphs
Name: perl-DBD-Chart
Version: 0.81
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-Chart/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DARNOLD/DBD-Chart-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-DBI, perl-GD, gd-devel, perl-GD-Text-Util

%description
The DBD::Chart provides a DBI abstraction for rendering pie charts, bar
charts, box&whisker charts (aka boxcharts), histograms, Gantt charts,
and line, point, and area graphs.

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DBD/Chart.pm
%{perl_vendorlib}/DBD/Chart

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.81-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.81-1
- Initial package.
