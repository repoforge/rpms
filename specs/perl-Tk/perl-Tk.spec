# $Id: perl-Tk.spec 1 2004-03-22 12:05:34Z bert $

# Authority: dag

# Upstream: ptk@lists.stanford.edu

Summary: Tk module for perl.
Name: perl-Tk
#Version: 800.024
Version: 804.026
Release: 0
License: GPL or Artistic
Group: Applications/CPAN
URL: http://www.perltk.org/
Summary: perl/Tk modules and tools

Packager: Bert de Bruijn <bert@debruijn.be>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://cpan.org/modules/by-module/Tk/Tk-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: perl
BuildRequires: tk-devel >= 8.0.0
Requires: perl

%description
Perl bindings to the Tk Graphical User Interface ToolKit. 

%prep
%setup -n Tk-%{version}

%build
find . -type f | xargs perl -pi -e 's|^#!.*/bin/perl\S*|#!/usr/bin/perl|'
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist
# these files require extra perl-Tk modules
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/Tk/reindex.pl
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/Tk/demos/LabEnLabRad.pm

%clean 
#%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL README* Changes MANIFEST ToDo
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*
%{_bindir}/*

%changelog
* Mon Mar 22 2004 Bert de Bruijn <bert@debruijn.be> - 804.026-0
- Initial package
