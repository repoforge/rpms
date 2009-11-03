# $Id$
# Authority: matthias

Summary: MMS Streams Recorder
Name: mmsrip
Version: 0.7.0
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://nbenoit.tuxfamily.org/projects.php?rq=mmsrip
Source: http://nbenoit.tuxfamily.org/projects/mmsrip/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
MMSRIP is a pure useless program which allows you to save on your hard-disk
the content being streamed by an MMS server. This program has been written
for personnal use, so don't blame me if you think I am stupid doing such
tool for the others.


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
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/mmsrip
%{_mandir}/man?/*


%changelog
* Fri Sep  8 2006 Matthias Saou <http://freshrpms.net/> 0.7.0-1
- Update to 0.7.0.

* Sat Jan 14 2006 Federico Simoncelli <federico.simoncelli@gmail.com>
- Initial release

