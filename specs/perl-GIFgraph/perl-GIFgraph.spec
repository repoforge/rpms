# $Id$
# Authority: dag
# Upstream: Martien Verbruggen <mverb$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name GIFgraph

Summary: Graph Plotting Module (deprecated)
Name: perl-GIFgraph
Version: 1.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GIFgraph/

Source: http://www.cpan.org/modules/by-module/GIFgraph/GIFgraph-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Image::Magick)

%description
Graph Plotting Module (deprecated).

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

### Clean up docs
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README samples/
%doc %{_mandir}/man3/GIFgraph.3pm*
%{perl_vendorlib}/GIFgraph/
%{perl_vendorlib}/GIFgraph.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 1.20-1
- Initial package. (using DAR)
