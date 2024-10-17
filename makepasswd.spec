%define _empty_manifest_terminate_build 0

Name: 		makepasswd
Version: 	1.10
Release:	1
Summary: 	Generate random passwords
License: 	GPL
Group: 		System/Configuration/Other
URL: 		https://www.defora.org/index.php?page=projects&project=makepasswd
Source0:    http://ftp.debian.org/debian/pool/main/m/makepasswd/makepasswd_%{version}.orig.tar.gz
#Source0: 	http://www.defora.org/os/download/3500/%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
Makepasswd generates pseudo-random passwords of a desired length. It is able
to generate its crypted equivalent.

%prep
%autosetup -n %{name}-%{version} -p1

%build
#nothing to build

%install
install -D -m0755 makepasswd %{buildroot}/usr/bin/makepasswd

%files
%{_bindir}/makepasswd


%changelog
* Mon Mar 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-1mdv2011.0
+ Revision: 648675
- new version

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-8mdv2011.0
+ Revision: 620292
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.4.2-7mdv2010.0
+ Revision: 429938
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 0.4.2-6mdv2009.0
+ Revision: 251791
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.4.2-4mdv2008.1
+ Revision: 140944
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import makepasswd


* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.2-4mdv2007.0
- %%mkrel

* Thu Jul 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.2-3mdk 
- spec cleanup
- correct optimisations

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.4.2-2mdk 
- rpmbuildupdate aware

* Sun Jan 25 2004 Austin Acton <austin@mandrake.org> 0.4.2-1mdk
- from Taj Morton <taj@wildgardenseed.com> :
  - First Package

