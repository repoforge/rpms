# $Id$

# Authority: dag
# Upstream: Markus F.X.J. Oberhumer <markus@oberhumer.com>

Summary: Real-time file compressor
Name: lzop
Version: 1.01
Release: 1
License: GPL
Group: Applications/Archiving
URL: http://www.lzop.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.lzop.org/download/lzop-%{version}.tar.gz
Patch0: lzop-1.01-gcc29.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: lzo-devel

%description
lzop is a compression utility which is designed to be a companion to gzip. It
is based on the LZO library and its main advantages over gzip are much higher
compression and decompression speed at the cost of compression ratio.

lzop was designed with reliability, speed and portability in mind and as a
reasonable drop-in compatiblity to gzip.

%prep
%setup
%patch0

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS NEWS README THANKS
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
