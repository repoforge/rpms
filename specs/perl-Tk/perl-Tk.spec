# $Id: perl-Tk.spec 1 2004-03-22 12:05:34Z bert $
# Authority: dag
# Upstream: <ptk@lists.stanford.edu>

%define perl_vendorlib  %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch  %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tk

Summary: Tk module for perl
Name: perl-Tk
Version: 804.026
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://www.perltk.org/

Packager: Bert de Bruijn <bert@debruijn.be>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://cpan.org/modules/by-module/Tk/Tk-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, tk-devel >= 8.0.0
Requires: perl

%description
Perl bindings to the Tk Graphical User Interface ToolKit. 

%prep
%setup -n %{real_name}-%{version}

%build
find . -type f -exec %{__perl} -pi -e 's|^#!/.*bin/perl\S*|#!%{__perl}|i;' {} \;
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot (arch)
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

### FIXME: These files require extra perl-Tk modules
#%{__rm} -f %{buildroot}%{perl_vendorarch}/Tk/reindex.pl
#%{__rm} -f %{buildroot}%{perl_vendorarch}/Tk/demos/LabEnLabRad.pm

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes COPYING INSTALL MANIFEST README* ToDo
%doc %{_mandir}/man?/*
%{_bindir}/*
%{perl_vendorarch}/*

%changelog
* Thu May 13 2004 Dag Wieers <dag@wieers.com> - 804.026-1
- Cosmetic changes.

* Mon Mar 22 2004 Bert de Bruijn <bert@debruijn.be> - 804.026-0
- Initial package
