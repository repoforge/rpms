# $Id$
# Authority: matthias
# Upstream: Matthias Czapla <dermatsch$gmx,de>

Summary: Convert files in CUE format to cdrdao's TOC format
Name: cue2toc
Version: 0.4
Release: 1%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://cue2toc.sourceforge.net/
Source: http://dl.sf.net/cue2toc/cue2toc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Small program to convert CUE files (understood by CDRWin) to cdrdao's TOC
format. Features include: support for complete set of CUE commands (e.g.
catalog number, data and audio tracks, ISRC codes, CD-Text, Pre-/Postgaps
(with zero data or data from file), subindexes etc.), automatic determination
of session type and conversion of data files by user configurable commands
based on file name extension matching.


%prep
%setup


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
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/cue2toc
%{_mandir}/man1/cue2toc.1*


%changelog
* Mon Aug  9 2004 Matthias Saou <http://freshrpms.net/> 0.4-1
- Initial RPM release.

