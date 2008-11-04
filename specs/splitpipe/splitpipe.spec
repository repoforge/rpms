# $Id$
# Authority: dag

Summary: Tool to allow streaming piped output to span multiple volumes
Name: splitpipe
Version: 0.4
Release: 1
License: GPL
Group: Applications/File
URL: http://ds9a.nl/splitpipe/

Source: http://ds9a.nl/splitpipe/splitpipe-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
splitpipe allows streaming piped output to span multiple volumes, which might
be floppies, cd-recordables, dvd's or whatnot.
joinpipe performs the reverse process. No temporary files are used.

Splitpipe accepts the output of, say, tar on standard input and distributes it
over multiple chunks. These chunks contain labels that guarantee integrity,
verify that the entire chunk is read, and that they are read in the proper
order.
This allows for the backup of full filesystems, at high speed.

%prep
%setup

%build
%{__make} %{?_smp_mflags} PREFIX="%{_prefix}" OPTFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" PREFIX="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING HACKING PLAN README TODO cdrecord-script doc/*.html
%doc %{_mandir}/man1/joinpipe.1*
%doc %{_mandir}/man1/splitpipe.1*
%doc %{_mandir}/man5/splitpipe.5*
%{_bindir}/splitpipe
%{_bindir}/joinpipe

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 0.4-1
- Initial package. (using DAR)
