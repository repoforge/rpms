# $Id$
# Authority: dag
# Upstream: Brian Carrier <carrier$sleuthkit,org>

Summary: Open Source forensic toolkit
Name: sleuthkit
Version: 1.69
Release: 1.2%{?dist}
License: GPL/IBM
Group: Applications/Internet
URL: http://www.sleuthkit.org/sleuthkit/

Source: http://dl.sf.net/sleuthkit/sleuthkit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The Sleuth Kit is a collection of UNIX-based command line file system
forensic tools that allow an investigator to examine NTFS, FAT, FFS,
EXT2FS, and EXT3FS file systems of a suspect computer in a non-intrusive
fashion.

The tools have a layer-based design and can extract data from internal
file system structures. Because the tools do not rely on the operating
system to process the file systems, deleted and hidden content is shown.

%prep
%setup

%build
%{__make} %{?_smp_mflags}  \
	prefix="%{_prefix}" \
	mandir="%{_mandir}" \
	datadir="%{_datadir}/sleuthkit" \
	DESTDIR="%{buildroot}"
cd src/file
%configure \
	--datadir="%{_datadir}/sleuthkit"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_mandir}/man1/
%{__install} -p -m0755 bin/* %{buildroot}%{_sbindir}
%{__install} -p -m0644 man/man1/* %{buildroot}%{_mandir}/man1/
%{__install} -p -m0755 src/file/src/file %{buildroot}%{_sbindir}
%{__ln_s} -f %{_sbindir}/file %{buildroot}%{_sbindir}/file_sk
#%{__mv} -f %{buildroot}%{_mandir}/man1/file.1 %{buildroot}%{_mandir}/man1/file_sk.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING LICENSE README TODO docs/* tct.docs/
%doc %{_mandir}/man?/*
%{_sbindir}/*
#%{_datadir}/sleuthkit/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.69-1.2
- Rebuild for Fedora Core 5.

* Sun May 30 2004 Dag Wieers <dag@wieers.com> - 1.69-1
- Updated to release 1.69.

* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 1.68-1
- Updated to release 1.68.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 1.65-1
- Updated to release 1.65.
- Fixed %%{_sbindir}/file

* Fri Aug 15 2003 Dag Wieers <dag@wieers.com> - 1.64-0
- Updated to release 1.64.

* Sun Jul 13 2003 Dag Wieers <dag@wieers.com> - 1.62-0
- Initial package. (using DAR)
