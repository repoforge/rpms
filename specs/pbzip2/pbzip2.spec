# $Id$
# Authority: dries
# Upstream: Jeff Gilchrist <pbzip2$compression,ca>

Summary: Parallel implementation of bzip2
Name: pbzip2
Version: 0.9.4
Release: 1
License: BSD
Group: Applications/File
URL: http://compression.ca/pbzip2/

Source: http://compression.ca/pbzip2/pbzip2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, bzip2-devel

%description
PBZIP2 is a parallel implementation of the bzip2 block- sorting file 
compressor that uses pthreads and achieves near-linear speedup on SMP 
machines.

%prep
%setup
%{__perl} -npi -e "s|.PREFIX./man|(PREFIX)/share/man|g;" Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall PREFIX=%{buildroot}%{_prefix}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%doc %{_mandir}/man?/*
%{_bindir}/pbzip2

%changelog
* Wed Aug 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.4-1
- Initial package.
